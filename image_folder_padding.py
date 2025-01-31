import cv2
import os
import numpy as np

import cv2
'''
test_image_path = 'C:/Users/haris/OneDrive/Desktop/scan/Διεθνές_Πανεπιστήμιο/Μηχανική_Μάθηση/Data/train_images/img_189317616199067.jpg'  # Αντικαταστήστε με την πραγματική διαδρομή μιας εικόνας
img = cv2.imread(test_image_path)
if img is not None:
    print("Η εικόνα φορτώθηκε επιτυχώς.")
else:
    print("Η εικόνα δεν μπόρεσε να φορτωθεί.")

def pad_images_in_folder(input_folder, output_folder, target_size=(224, 224)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Φιλτράρισμα για εικόνες
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)
            old_size = img.shape[:2]  # Παλιό μέγεθος

            # Διαστάσεις για padding
            delta_w = target_size[1] - old_size[1]
            delta_h = target_size[0] - old_size[0]
            top, bottom = delta_h // 2, delta_h - (delta_h // 2)
            left, right = delta_w // 2, delta_w - (delta_w // 2)
            print("Τιμές για padding:", top, bottom, left, right)
            # Εφαρμογή padding
            color = [0, 0, 0]  # Μαύρο χρώμα για padding
            new_img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

            # Αποθήκευση της νέας εικόνας
            new_img_path = os.path.join(output_folder, filename)
            cv2.imwrite(new_img_path, new_img)
'''
import cv2
import os

def find_largest_image_size(input_folder):
    max_width = 0
    max_height = 0
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.png')):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                height, width = img.shape[:2]
                if width > max_width or height > max_height:
                    max_width, max_height = width, height
    return max_width, max_height

def pad_images_to_size(input_folder, output_folder, target_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.png')):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                old_size = img.shape[:2]
                delta_w = target_size[0] - old_size[1]
                delta_h = target_size[1] - old_size[0]
                top, bottom = delta_h // 2, delta_h - (delta_h // 2)
                left, right = delta_w // 2, delta_w - (delta_w // 2)
                color = [0, 0, 0]
                try:
                    new_img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
                except:
                    print(img_path)
                new_img_path = os.path.join(output_folder, filename)
                cv2.imwrite(new_img_path, new_img)

os.chdir('C:\\Users\\haris\\OneDrive\\Desktop\\scan\\Διεθνές_Πανεπιστήμιο\\Μηχανική_Μάθηση\\Data')

# Καθορίστε τους φακέλους εισόδου και εξόδου
input_folder = 'test_images'
output_folder = 'test_padding_images'

# Βρείτε τις διαστάσεις της μεγαλύτερης εικόνας
#largest_width, largest_height = find_largest_image_size(input_folder)
largest_width, largest_height =2850,2650
# Κάντε padding στις εικόνες στο μέγεθος της μεγαλύτερης εικόνας
pad_images_to_size(input_folder, output_folder, (largest_width, largest_height))

# Χρήση της συνάρτησης
#input_folder = 'C:/Users/haris/OneDrive/Desktop/scan/Διεθνές_Πανεπιστήμιο/Μηχανική_Μάθηση/Data/train_images'
#output_folder = 'C:\\Users\\haris\\OneDrive\\Desktop\\scan\\Διεθνές_Πανεπιστήμιο\\Μηχανική_Μάθηση\\Data\\padding_images'
#pad_images_in_folder('train_images', 'padding_images')
