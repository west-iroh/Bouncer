# Bouncer - A Discord Bot
Allows you to create an 18+ 'gateway channel' for your discord server. 
Simply prompt new users to enter their age in this channel and Bouncer will handle the rest.

- If the user gives an integer >= 18, Bouncer will grant them a role of your choosing.
- If the user gives an integer < 18, Bouncer will ban them.
- If the user sends any other message content, Bouncer ignores them.

In all cases, Bouncer quickly deletes their message.
All of these actions can be logged by Bouncer in a channel of your choosing.

## Usage

### Commands

All commands can only be used by the owner or a user with the "Administrator" permission.

- `/bouncer set welcome_role [role]` sets the role to be granted to new users.
- `/bouncer set welcome_channel [channel]` sets the channel to be used as the 'gateway'.
- `/bouncer set log_channel [channel]` sets the channel to log Bouncer's actions.
- `/bouncer set exempt_roles [role-a role-b ... role-z]` sets a list roles that Bouncer will ignore.
(i.e. Bouncer will not attempt to ban them or will not delete their messages in the *welcome_channel*).
If you provide no roles, then it will set it to an empty list (no exempt roles).

<br/>
 
- `/bouncer get welcome_role` tells you the *welcome_role*.
- `/bouncer get welcome_channel` tells you the *welcome_channel*.
- `/bouncer get log_channel` tells you the *log_channel*.
- `/bouncer get exempt_roles` tells you the *exempt_roles*.

<br/>

- `/bouncer disable welcome_role` sets the *welcome_role* to None.
- `/bouncer disable welcome_channel` sets the *welcome_channel* to None.
- `/bouncer disable log_channel` sets the *log_channel* to None.

<br/>

- `/bouncer help`
- `/bouncer ping`

### Permissions

Bouncer needs the "Manage Roles" and "Ban Members" permission.

- In the *welcome_channel* Bouncer needs "Read Messages" and "Manage Messages".
- In the *log_channel* Bouncer needs "Read Messages" and "Send Messages".
- In the channel you wish to execute Bouncer's commands, Bouncer needs "Read Messages" and "Send Messages".
