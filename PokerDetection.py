import cv2
import cvzone
import numpy 
from ultralytics import YOLO
from PokerFunction import findPokerHand
import os




model = YOLO(r".\model\playingCards.pt")

cap = cv2.VideoCapture(r".\source\PokerHands.mp4")

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

output_dir = r'.\detection'
output_file = os.path.join(output_dir, "Poker_Detection.mp4")

os.makedirs(output_dir, exist_ok=True)

out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*"mp4v"),fps,(frame_height,frame_width))


if not cap.isOpened():
    print("Video Error")
    exit()

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    results = model(frame, conf=0.5)[0]

    hand_collection = []

    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
        cv2.rectangle(frame,(int(x1), int(y1)), (int(x2), int(y2)),(0,255,0),3)


        card_name = results.names[int(box.cls[0])]

        hand_collection.append(card_name)

    hand_collection = list(set(hand_collection))

    if len(hand_collection) == 5:
        poker_hand_name = findPokerHand(hand_collection)
        cv2.putText(frame, f"Hand: {poker_hand_name}", (50, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3)  

    out.write(frame)
    cv2.imshow("Poker Hand Detection",  frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()