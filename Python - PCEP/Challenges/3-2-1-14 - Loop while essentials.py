blocks = int(input("Enter the number of blocks: "))
height = 0
blocks_Needed = 0 

#
# Write your code here.
#	

while blocks_Needed <= blocks:
    height += 1
    blocks_Needed += height
    
print("The height of the pyramid: ", height - 1)

# Baseline for this exercise that I deduced: 
#
# Initializing the variables:
#   heights = 1
#   blocks  = 0
#
# Formula to calculate blocks is designed down here: 
#
#   blocks_Needed = blocks_Needed + height
#   height += 1-2-1-   