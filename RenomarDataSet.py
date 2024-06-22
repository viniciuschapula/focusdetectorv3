import os

def rename_files_with_count(folder_path):
    # List all files in the given directory
    files = os.listdir(folder_path)
    
    # Filter images and text files, assuming common image extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    text_extension = '.txt'
    
    # Create lists to store image and text file paths
    image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
    text_files = [f for f in files if os.path.splitext(f)[1].lower() == text_extension]
    
    # Initialize a counter for the new filenames
    count = 1
    
    for image_file in image_files:
        # Get the base name without the extension
        base_name = os.path.splitext(image_file)[0]
        
        # Construct the corresponding text file name
        corresponding_text_file = base_name + text_extension
        
        # Check if the corresponding text file exists
        if corresponding_text_file in text_files:
            # Define the new base name with count
            new_base_name = f"PratoPlanta_{count}"
            
            # Construct the new image and text file names
            new_image_name = new_base_name + os.path.splitext(image_file)[1]
            new_text_name = new_base_name + text_extension
            
            # Get full paths
            old_image_path = os.path.join(folder_path, image_file)
            old_text_path = os.path.join(folder_path, corresponding_text_file)
            new_image_path = os.path.join(folder_path, new_image_name)
            new_text_path = os.path.join(folder_path, new_text_name)
            
            # Rename the files
            os.rename(old_image_path, new_image_path)
            os.rename(old_text_path, new_text_path)
            
            # Increment the counter
            count += 1
    
    print(f"Renaming completed. {count-1} pairs of files were renamed.")

# Example usage
folder_path = 'C:\\focusdetectorv3\\dataset_full\\Prato_de_vaso_de_planta'  # Change this to the path of your folder
rename_files_with_count(folder_path)