import pexpect
import os


# loop=True

# while loop:


# Set the environment variable
os.environ['DYLD_LIBRARY_PATH'] = '/opt/IriTech/IDDK-2000-3.3.1-OSX/demo/source:' + os.environ.get('DYLD_LIBRARY_PATH', '')

# Path to the executable
executable = '/opt/IriTech/IDDK-2000-3.3.1-OSX/demo/source/Iddk2000Demo'

# Start the process
child = pexpect.spawn(executable)
child.logfile = open('pexpect.log', 'wb')

# Interact with the process
child.expect("Please press ENTER to continue ...")
child.sendline("")

# Reset on open device: 
# 	1. Yes (default)
# 	2. No

child.expect("Enter your choice: ")
child.sendline("1")

# MAIN MENU: Select one of the features below
# 	1. Login
# 	2. Logout
# 	3. Device Management
# 	4. Device & SDK Information
# 	5. Capturing Process
# 	6. Iris Recognition
# 	7. Power Management
# 	8. Recovery (IriShield USB only)
# 	9. Exit
# Enter your choice:


child.expect("Enter your choice: ")
child.sendline("5")


# Parameters for capturing process
# Capture mode: 
# 	1. IDDK_TIMEBASED (default) 
# 	2. IDDK_FRAMEBASED
# Enter your choice: 


child.expect("Enter your choice: ")
child.sendline("1")


# Enter the duration since iris detected (from 1 to 600 seconds, enter for 3): 5

child.expect(r"Enter the duration since iris detected \(from 1 to 600 seconds, enter for 3\): ")
child.sendline("5")

# Quality mode: 
# 	1. Normal (default)
# 	2. High 
# 	3. Very High
# Enter your choice:

child.expect("Enter your choice: ")
child.sendline("2")

# Enable auto led? 
# 	1. Yes (default)
# 	2. No
# Enter your choice:


child.expect("Enter your choice: ")
child.sendline("1")





child.expect("Put your eyes in front of the camera")


print("""Put your eyes in front of the camera
    Scanning for eyes............................""")



# Simulate waiting for the eye scanning process
loop_to_capture=True
while loop_to_capture:

    index=child.expect(["Error: IDDK_SE_NO_QUALIFIED_FRAME","Error: IDDK_SE_NO_FRAME_AVAILABLE","Do you want to get the result image?"])

    
    if index==0 or index==1:

        # MAIN MENU: Select one of the features below
        # 	1. Login
        # 	2. Logout
        # 	3. Device Management
        # 	4. Device & SDK Information
        # 	5. Capturing Process
        # 	6. Iris Recognition
        # 	7. Power Management
        # 	8. Recovery (IriShield USB only)
        # 	9. Exit
        # Enter your choice:


        child.expect("Enter your choice: ")
        child.sendline("5")


        # Parameters for capturing process
        # Capture mode: 
        # 	1. IDDK_TIMEBASED (default) 
        # 	2. IDDK_FRAMEBASED
        # Enter your choice: 


        child.expect("Enter your choice: ")
        child.sendline("1")


        # Enter the duration since iris detected (from 1 to 600 seconds, enter for 3): 5

        child.expect(r"Enter the duration since iris detected \(from 1 to 600 seconds, enter for 3\): ")
        child.sendline("5")

        # Quality mode: 
        # 	1. Normal (default)
        # 	2. High 
        # 	3. Very High
        # Enter your choice:

        child.expect("Enter your choice: ")
        child.sendline("2")

        # Enable auto led? 
        # 	1. Yes (default)
        # 	2. No
        # Enter your choice:


        child.expect("Enter your choice: ")
        child.sendline("1")





        child.expect("Put your eyes in front of the camera")


        print("""Put your eyes in front of the camera
            Scanning for eyes............................""")

        loop_to_capture=True
        continue

    elif index==2:
        loop_to_capture=False


# Do you want to get the result image? 
# 	1. No (default)
# 	2. Yes
# Enter your choice: 2

child.expect("Enter your choice: ")
child.sendline("2")

# Select image kind: 
# 	1. Original Image - K1 (default) 
# 	2. VGA Image - K2 
# 	3. Cropped Image - K3
# 	4. Cropped and Masked Image - K7
# Enter your choice:

child.expect("Enter your choice: ")
child.sendline("1")


# Select image format: 
# 	1. Mono JP2 Image (default)
# 	2. Mono Raw Image
# 	3. IriTech JP2 Image
# 	4. IriTech Raw Image
# Enter your choice: 1


child.expect("Enter your choice: ")
child.sendline("1")

# Enter compress ratio (enter for default): 50


child.expect("Enter compress .*: ")
child.sendline("50")


# Do you want to get result ISO image: 
# 	1. No (default)
# 	2. Yes
# Enter your choice:

child.expect("Enter your choice: ")
child.sendline("1")

# Close the log file
child.logfile.close()

child=pexpect.spawn("mv /opt/IriTech/IDDK-2000-3.3.1-OSX/demo/source/UnknownEyeImage_1.jp2 /Users/czajkademo1/Desktop/pyDemo/LeftEye.jp2")
child.logfile.close()
print("Process completed.")

    # do_continue=input("Enter q to quit anything else to continue: ")
    # if do_continue.lower()!="q":
    #     loop=True
    # else:
    #     loop=False

