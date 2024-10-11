from collections import deque

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list of lists): A list of boxes where each box is a list of keys.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    # Initialize a set to keep track of opened boxes
    opened = set()
    
    # Initialize a queue with the first box
    queue = deque([0])
    
    # Mark the first box as opened
    opened.add(0)
    
    # While there are still boxes to open
    while queue:
        # Get the next box
        box = queue.popleft()
        
        # For each key in the box
        for key in boxes[box]:
            # If the key is valid and the box is not already opened
            if key < len(boxes) and key not in opened:
                # Mark the box as opened
                opened.add(key)
                # Add the box to the queue
                queue.append(key)
    
    # Return True if all boxes are opened, False otherwise
    return len(opened) == len(boxes)
