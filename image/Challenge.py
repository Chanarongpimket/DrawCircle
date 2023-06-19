import cv2
import numpy as np

def draw_line(image, start_point, end_point, brush_style, brush_size):
    # Convert the points to integer values
    start_point = (int(start_point[0]), int(start_point[1]))
    end_point = (int(end_point[0]), int(end_point[1]))

    # Select the brush style
    if brush_style == 'solid':
        line_type = cv2.LINE_AA
    elif brush_style == 'dotted':
        line_type = cv2.LINE_4
    elif brush_style == 'dashed':
        line_type = cv2.LINE_8

    # Draw the line on the image
    cv2.line(image, start_point, end_point, (0, 0, 255), thickness=brush_size, lineType=line_type)

    # Show the image with the drawn line
    cv2.imshow("Image", image)
    cv2.waitKey(delay=7000)
    cv2.destroyAllWindows()

# Create a blank image
image = np.zeros((1000, 1000, 3), dtype=np.uint8)

# Get user input for start and end points
start_x = int(input("Enter the x-coordinate of the start point: "))
start_y = int(input("Enter the y-coordinate of the start point: "))
end_x = int(input("Enter the x-coordinate of the end point: "))
end_y = int(input("Enter the y-coordinate of the end point: "))
start_point = (start_x, start_y)
end_point = (end_x, end_y)

# Get user input for brush style
brush_style = input("Enter the brush style (solid, dotted, dashed): ")

# Get user input for brush size
brush_size = int(input("Enter the brush size: "))

# Draw the line
draw_line(image.copy(), start_point, end_point, brush_style, brush_size)
