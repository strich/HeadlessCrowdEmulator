HeadlessCrowdEmulator
=====================

Wrapper scripts for running and crowd sourcing emulated games on a headless linux server, then live streaming it to twitch.

In order to achieve this we utilize XVFB to create a virtual frame buffer on which we can display the desktop and any desktop applications on a headless VM hosted anywhere.
I use the VBA-M (http://sourceforge.net/projects/vbam) emulator to emulate basic gameboy games such as Pokemon.
The AVConv tools are used to capture the audio and video from the virtual frame buffer and live streamed to Twitch.

Finally, I have created a small set of Python scripts to manage the remote key presses of thousands of users. It has support for Democracy and Anarchy modes. By default anarchy mode is in effect and will pass on the newest key press to the emulator. If democracy mode is voted high enough over anarchy, it will switch to buffering key presses and only sending the most popular one every 10 seconds. Democracy mode decays back to anarchy over time if it is not consistently voted for.

There is a simple web-frontend managed by Tornado that will display the twitch stream, twitch chat, and the web-based gameboy controller. FYI it is unfinished and only some buttons ended up be wired up.

Setup
=====================

On a typical Linux (uBuntu or Debian) install you will need:
apt-get install xvfb avconv libav-tools alsa-utils xdotool python-pip

You will need to go grab Facebook's Tornado (https://github.com/facebook/tornado) for the remote key press stuff.

Run
=====================

1. Initialize xvfb: ./load_xvfb.sh
2. Run the emulator: ./load_emulator.sh
3. Start the twitch stream: ./twitch_streamer.sh
4. Start the InputManager: python www_crowdEmulator/main.py
