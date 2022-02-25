## wireguard-helpers
A collection of scripts to automate the process of creating WireGuard-tunnels.

You can
- Create servers
- Create peers         
-  Authorize peers
- Deauthorize peers
- Delete interfaces

Clone the repository and run `sudo ./install.py` as root or a user with sudo-rights.
   
Then, you can run `sudo wg-helper` as root or a user with sudo-rights to automate your work with WireGuard.

There is also a non-interactive mode.
The Syntax is as follows:

`./wg-helper.py <ACTION> <ARGUMENTS>`

Actions:

` --add-peer-interface
` 
to add a peer-interface to connect to an existing server.

`--add-server-interface` to create a new WireGuard-Server



You can copy this code, fork it or do anything else with it, as long as it's not used commercially.

Happy networking!
