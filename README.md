# mapGame

In this game we have a target goal location and a player location that is being tracked.  
While running the game on your phone your location is updated and you can see how far away you are from your goal.  
Currently the goal is located somewhere inside the **STC Building**.

---

## How does it all work?

The game is being run on an **Oracle Cloud Virtual Machine**.  
The machine is running the `mapGame.py` and the `Index.html`.

### `mapGame.py`

- This file is what sets the goal location for the game.
- It has an update location function that requests data to be sent out to Google.
- It waits to see if the player is within 10 meters before announcing you have won.

### `Index.html`

- This site is updated every five seconds checking the location of the player.
- It displays how far away the goal is and will change to a victory screen once you have arrived.

---

## How to play

The game is currently running on the cloud right now!  
If you want to try it out simply go to this URL:  
**[https://76cd-141-148-176-231.ngrok-free.app](https://76cd-141-148-176-231.ngrok-free.app)**

Once you are there you will receive a request to share your location.  
Hit yes and the game will update to show how far away you are.  
Every five seconds you will see your location update.

> Have fun walking about the STC building and finding the goal.

---

## How it all works and Issues I ran into

As I have stated before, the game is all run off of a virtual machine.  
I have set up TCP rules to allow traffic on specific ports to allow data to be passed to the machine and the player.

Initially I had the player connecting directly to the VM which seemed like it would be fine, but I got an interesting error from Google.  
It was not willing to send data back to just a random IP address.  
Since my VM is just some random IP address I had to find a middle man to help the program and Google communicate.

I could have bought my own domain but I was not willing to put some money out for this project, so instead I learned about a free tool called **Ngrok**.  
This program will stand in between my program and Google and handle the traffic between the two.  
It provides me with an IP address that Google recognizes as safe.  
It can send the request for location updates to Google and pass the data back to the program in order to allow the player to be tracked.

