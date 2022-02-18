SCREEN_WIDTH = 800
SCREEN_LENGTH = 600

def check_if_within_screen_limit(curr_x, curr_y):
    print(" check screen limit at ", curr_x, curr_y, SCREEN_LENGTH, SCREEN_WIDTH)
    if curr_x >= 0 and curr_y >= 0 and curr_y <= SCREEN_LENGTH and curr_x <= SCREEN_WIDTH:
        return True
    return False