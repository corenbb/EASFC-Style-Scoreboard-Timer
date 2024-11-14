import time
import sys

def countdown(in_game_duration=90, real_time_duration=1, halftime_duration=15, added_time_first_half=2, added_time_second_half=3):
    total_real_seconds = real_time_duration * 60
    interval = total_real_seconds / (in_game_duration * 60)

    first_half_duration = in_game_duration // 2
    first_half_end = first_half_duration + added_time_first_half

    second_half_duration = in_game_duration - first_half_duration
    second_half_end = in_game_duration + added_time_second_half

    def display_time(minute, second):
        sys.stdout.write(f"\rIn-Game time: {minute:02}:{second:02}")
        sys.stdout.flush()

    def wait_for_user(prompt):
        input(prompt)

    for in_game_second in range(first_half_end * 60):
        in_game_minutes = in_game_second // 60
        in_game_seconds = in_game_second % 60
        display_time(in_game_minutes, in_game_seconds)
        time.sleep(interval)

    print("\n Half-time!")
    wait_for_user("Press Enter to start the second half...")

    for in_game_second in range(first_half_end * 60, second_half_end * 60):
        in_game_minutes = in_game_second // 60
        in_game_seconds = in_game_second % 60
        display_time(in_game_minutes, in_game_seconds)
        time.sleep(interval)


    print("\n Full-time!")

countdown(in_game_duration=90, real_time_duration=1, halftime_duration=15, added_time_first_half=2, added_time_second_half=3)