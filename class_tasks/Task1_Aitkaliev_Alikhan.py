import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Can't open camera")
    exit()
while True:
    ret, frame = cap.read()

    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame, "Alikhan", (20,250), font, 2, (255,255,255), 2, cv.LINE_AA)

    cv.imshow("Frame", frame)

    k=cv.waitKey(1)

    if k==ord("s"):
        cv.imwrite("photo.png", frame)
    elif k & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()