# lite-60

Hi Doug,
Brooke found https://timeqube.com/ and asked if we could help make a stress-free timer for 60 minute counseling session

I have a microcontroller https://wiki.seeedstudio.com/XIAO-RP2040/ configured and running code 
using the complier Thonny https://thonny.org/
and editing the code in Notepad ++ with the language set to Python

The revision Wishlist:
rev.1
	-change the Python shell code from a "cycle timer" displaying different LED values (colors) for a set duration to an event-based timer
		-the 4 events are:
			-"majority of time remaining" (green LED value)
			-"half or less than half of time remaining" (yellow LED value)
			-"closing thoughts and topics for next session" (solid red LED value)
			-"session is over" (flashing red LED value)
