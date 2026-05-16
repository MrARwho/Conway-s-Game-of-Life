def TOH (numbers , start , mid, end ):
    if numbers == 1:
        print (f"Move disk 1 from {start} to {end}")
        return
    #move top n-1 disks from start to mid using end
    TOH (numbers - 1 , start , end , mid)
    print (f"Move disk {numbers} from {start} to {end}")
    #move n-1 disks from mid to end using start
    TOH (numbers - 1 , mid , start , end)
    
disks = 5
TOH (disks , 'A' , 'B' , 'C')