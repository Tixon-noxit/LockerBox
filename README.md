# LockerBox #
Program for monitoring payments for cells leased
The program maintains its database and counts the number of remaining days of paid rent. 
After the lease expires, it changes the status of the cell on its own, informing the user about it.

## Graphic display of cell statuses ##
At the top of the screen

The user has 60 cells. Each cell has the following states:
  With spare key(Image of the key on the cell):
    - Free (White);
    - Busy and paid (Green);
    - Busy and overdue (Red);
    - Broken (Yellow);
    
  No spare key(The key image is missing from the cell):
    - Free (White);
    - Busy and paid (Green);
    - Busy and overdue (Red);
    - Broken (Yellow);
    
   
   
## Information table ## 
Located at the bottom of the screen

The table displays general data on frames: 
  -The situation as a whole 
  -Tenants 
  -Cells with overdue payments 
  -Cells with missing spare keys
