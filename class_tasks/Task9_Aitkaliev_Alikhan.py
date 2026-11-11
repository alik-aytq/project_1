import cv2
cam = cv2.VideoCapture(0)

while True:
    ok, img = cam.read()

    if not ok:
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    green1 = (35, 50, 50)
    green2 = (85, 255, 255)

    mask = cv2.inRange(hsv, green1, green2)

    shapes, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for shape in shapes:
        if cv2.contourArea(shape) > 1000:
            x, y, w, h = cv2.boundingRect(shape)

            area = w * h

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.putText(img, f"Area: {area}", (x, max(y - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("window", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break