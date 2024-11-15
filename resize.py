from PIL import Image
import os
from config import *

def make_dirs_if_not_exist( dir_paths ):
    # if dir_path is a list
    if isinstance( dir_paths, list ):
        for dir_path in dir_paths:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
    else:
        if not os.path.exists(dir_paths):
            os.makedirs(dir_paths)

def add_trailing_slash_to_dirname(dirname):
    # Check if dirname is a valid directory name
    if dirname == '.' or not dirname.strip():
        return dirname  # Return as is for current directory or empty/whitespace

    # Add a trailing slash if it doesn't already have one
    if not dirname.endswith('/'):
        return dirname + '/'
    
    return dirname  # Return unchanged if it already ends with a slash

def resize_images( source_dirpath, resized_dest_dirpath, cropped_dest_dirpath ):
    # Create the output directories if they don't exist
    make_dirs_if_not_exist( [resized_dest_dirpath, cropped_dest_dirpath] )

    # Iterate through each files and subdirectories in the source directory
    for root, _, files in os.walk( source_dirpath ):

        print("Source: ", source_dirpath)
        print("root: ", root)

        # Calculate the destination path
        # This removes the source_dirpath part from the root
        relative_path = os.path.relpath( root, source_dirpath )
        print("relative_path: ", relative_path)

        # Calculate new subdirectory path
        resized_subdir_path = os.path.join( resized_dest_dirpath, relative_path )
        cropped_subdir_path = os.path.join( cropped_dest_dirpath, relative_path )
        print("resized_subdir_path: ", resized_subdir_path)
        print("cropped_subdir_path: ", cropped_subdir_path)
        
        # Create the subdirectories in the destination
        os.makedirs( resized_subdir_path, exist_ok=True )
        if( CROP_ENABLED ):
            os.makedirs( cropped_subdir_path, exist_ok=True )

        # Iterate through each files in current directory
        for filename in files:
            filepath = os.path.join(root, filename)
            resized_filepath = os.path.join(resized_subdir_path, os.path.splitext(filename)[0] + "." + IMG_FORMAT)
            cropped_filepath = os.path.join(cropped_subdir_path, os.path.splitext(filename)[0] + "." + IMG_FORMAT)
            """ print("---")
            print("filepath: ", filepath)
            print("resized_filepath: ", resized_filepath)
            print("cropped_filepath: ", cropped_filepath) """

            # Open the image file
            with Image.open( filepath ) as img:

                imgWidth, imgHeight = img.size

                # set default values
                new_width = imgWidth
                new_height = imgHeight

                # If fixed side is set to height or width
                if RESIZE_FIXED_SIDE == 'height':
                    new_height = RESIZE_FIXED_SIDE_PX
                    # Calculate the new width
                    new_width = int( round( ( imgWidth / imgHeight ) * new_height ) )
                elif RESIZE_FIXED_SIDE == 'width':
                    new_width = RESIZE_FIXED_SIDE_PX
                    # Calculate the new height
                    new_height = int( round( ( imgHeight / imgWidth ) * new_width ) )

                # Resize the image
                img = img.resize( ( new_width, new_height ) )

                # Rotate image
                if( ROTATE_IMAGE ):
                    img = img.rotate( ROTATE_ANGLE, expand=True )

                # Convert to RGB if IMG_FORMAT = "webp"
                if IMG_FORMAT == 'webp' and img.mode != 'RGB':
                    img = img.convert('RGB')

                # Save image as webp
                img.save( resized_filepath, format=IMG_FORMAT )

                print("Done resized_filepath: ", resized_filepath)

        print("=======================")