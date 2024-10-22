import qrcode
from PIL import Image, ImageDraw
import random

def create_shopping_cart_qr(url, output_file):
    # Create QR code instance
    qr = qrcode.QRCode(version=None, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    # Get QR code matrix
    matrix = qr.get_matrix()

    # Set up colors
    bg_color = "#FFFFFF"  # White background
    cart_color = "#4A90E2"  # Blue for cart
    wheel_color = "#F5A623"  # Orange for wheels
    item_colors = ["#FF6B6B", "#50E3C2", "#59CD90", "#FAC05E"]  # Colors for items in cart

    # Calculate cell size
    cell_size = 10
    size = len(matrix) * cell_size

    # Create image
    image = Image.new("RGB", (size, size), bg_color)
    draw = ImageDraw.Draw(image)

    # Draw QR code with custom patterns
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]:
                x, y = col * cell_size, row * cell_size

                # Randomly choose between cart, wheel, or item
                choice = random.randint(0, 10)

                if choice == 0:  # Draw cart
                    draw.rectangle([x, y, x + cell_size, y + cell_size * 0.7], fill=cart_color)
                    draw.polygon([x, y + cell_size * 0.7, x + cell_size, y + cell_size * 0.7,
                                  x + cell_size * 0.8, y + cell_size], fill=cart_color)
                elif choice == 1:  # Draw wheel
                    draw.ellipse([x, y, x + cell_size, y + cell_size], fill=wheel_color)
                else:  # Draw item
                    item_color = random.choice(item_colors)
                    draw.rectangle([x, y, x + cell_size, y + cell_size], fill=item_color)

    # Save the image
    image.save(output_file)

# Usage
website_url = "https://www.google.com"
output_file = "shopping_cart_qr_code.png"
create_shopping_cart_qr(website_url, output_file)
