import os
import shutil

subs_folder = 'E:\\Invincible_S01_Subs'
episodes_folder = 'E:\\Invincible (2021) Season 1'
subs_ext = '.srt'
episodes_ext = '.mkv'
subs_files = os.listdir(subs_folder)
episodes_files = os.listdir(episodes_folder)
subs_filtered = [file for file in subs_files if file.endswith(subs_ext)]
episodes_filtered = [file for file in episodes_files if file.endswith(episodes_ext)]

subs_files = sorted(subs_filtered)
episodes_files = sorted(episodes_filtered)

if len(subs_files) != len(episodes_files):
    print('Number of episodes and subs do not match')
    exit()
else:
    for sub_file, episode_file in zip(subs_files, episodes_files):
        sub_path = os.path.join(subs_folder, sub_file)
        episode_path = os.path.join(episodes_folder, episode_file)

        new_sub_path = os.path.join(episodes_folder, os.path.splitext(episode_file)[0] + subs_ext)

        shutil.move(sub_path, new_sub_path)
