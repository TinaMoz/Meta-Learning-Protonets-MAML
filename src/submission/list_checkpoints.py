import os

def list_checkpoints(log_dir):
    checkpoints = []
    for file in os.listdir(log_dir):
        if file.startswith("state") and file.endswith(".pt"):
            step = int(file[len("state"):-len(".pt")])
            checkpoints.append(step)
    return sorted(checkpoints)

# List checkpoints for both log directories
checkpoints_1_shot = list_checkpoints('logs/5_way_1_shot')
checkpoints_5_shot = list_checkpoints('logs/5_way_5_shot')

print(f'Available checkpoints for 5-way 1-shot: {checkpoints_1_shot}')
print(f'Available checkpoints for 5-way 5-shot: {checkpoints_5_shot}')
