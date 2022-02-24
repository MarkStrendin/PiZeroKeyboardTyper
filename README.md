# Pi Zero Keyboard Typer
Code to make a Raspberry Pi Zero emulate a keyboard and type strings. 
This apparently only works on a Pi Zero, not other Pis, because of the USB chipset used. I have written and tested this on a Raspberry Pi Zero W (version 1).
This could be used to type passwords or commands remotely, given that the Raspberry Pi can be connected to the network. You could also configure this script to run on startup, so that no interaction is required. You could also turn this into a "Bash Bunny" type device, and use it as a network implant.

This is based on a tutorial that I found and adapted here: https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/. This tutorial worked, but I was not happy with the example code, so here we are.

# Setting up the Pi
Image an SD card with Raspberry Pi OS Lite, and set it up so that you can access it with SSH or a keyboard.

Type the following commands at a command prompt:
```
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules
sudo touch /usr/bin/isticktoit_usb
sudo chmod +x /usr/bin/isticktoit_usb
```

Now edit `/etc/rc.local`:

```
sudo nano /etc/rc.local
```

and add the following code just before the `exit 0` at the bottom:
```
/usr/bin/isticktoit_usb # libcomposite configuration
```

Now create the "gadget" code to configure how the Pi is detected as a USB device:
```
sudo nano /usr/bin/isticktoit_usb
```

```bash
#!/bin/bash
cd /sys/kernel/config/usb_gadget/
mkdir -p isticktoit
cd isticktoit
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
mkdir -p strings/0x409
echo "1234567890123456" > strings/0x409/serialnumber
echo "John Smith" > strings/0x409/manufacturer
echo "Totally legit keyboard" > strings/0x409/product
mkdir -p configs/c.1/strings/0x409
echo "Config 1: ECM network" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower

# Add functions here
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/
# End functions

ls /sys/class/udc > UDC
```

Now __reboot__ your Pi.

# Running the code
You need to be `sudo` to run the code, because of the device that this accesses in Linux. There may be a way around this - I am not sure, and have not looked into it so far. Maybe I'll explore this and update this file one day. Maybe not.

| Function                           | Description                                      |
|------------------------------------|--------------------------------------------------|
| send_keystroke("a")                | Types a single key. Unknown keys are ignored.    |
| send_phrase("Hello")               | Types a word or phrase.                          |
| send_phrase_with_enter("Hello")    | Types a word or phrase and then presses enter.   |
| send_phrase_with_tab("Hello")      | Types a word or phrase and then presses tab.     |
| send_enter()                       | Presses the enter key.                           |
| send_tab()                         | Presses the tab key.                             |

# See also

Tutorial that this code is based on: https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/
Keyboard codes, in case more keys need to be added: https://www.win.tue.nl/~aeb/linux/kbd/scancodes-10.html#scancodesets
