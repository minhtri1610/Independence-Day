import pygame
import math
import time

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chào Mừng 79 Năm Ngày Quốc Khánh CHXHCN Việt Nam")

# Màu sắc
RED = (218, 37, 29)
YELLOW = (255, 255, 0)

# Vẽ ngôi sao
def draw_star(surface, color, center, size, fill_percentage=100):
    points = []
    for i in range(5):
        angle = math.pi * 2 * i / 5 - math.pi / 2
        point = (
            center[0] + size * math.cos(angle),
            center[1] + size * math.sin(angle)
        )
        points.append(point)
        
        inner_angle = angle + math.pi / 5
        inner_point = (
            center[0] + size * 0.38 * math.cos(inner_angle),
            center[1] + size * 0.38 * math.sin(inner_angle)
        )
        points.append(inner_point)
    
    # Tính toán số điểm cần vẽ dựa trên phần trăm lấp đầy
    num_points = max(3, int(len(points) * fill_percentage / 100))
    if num_points > 2:
        pygame.draw.polygon(surface, color, points[:num_points])

# Vòng lặp chính
running = True
fill_percentage = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa màn hình
    screen.fill((0, 0, 0))  # Đặt nền đen

    # Vẽ nền đỏ với hiệu ứng lấp đầy
    fill_width = int(WIDTH * fill_percentage / 100)
    pygame.draw.rect(screen, RED, (0, 0, fill_width, HEIGHT))

    # Vẽ ngôi sao vàng với hiệu ứng lấp đầy
    star_center = (WIDTH // 2, HEIGHT // 2)
    star_size = min(WIDTH, HEIGHT) // 5
    star_fill = max(0, min(100, (fill_percentage - 50) * 2))  # Giới hạn từ 0 đến 100
    if star_fill > 0:
        draw_star(screen, YELLOW, star_center, star_size, star_fill)

    # Cập nhật màn hình
    pygame.display.flip()

    # Tăng phần trăm lấp đầy
    if fill_percentage < 100:
        fill_percentage += 0.5  # Giảm tốc độ lấp đầy
    else:
        time.sleep(1)  # Dừng 1 giây khi hoàn thành
        fill_percentage = 0  # Reset để lặp lại hiệu ứng

    clock.tick(60)  # Giới hạn 60 khung hình/giây

# Kết thúc Pygame
pygame.quit()
