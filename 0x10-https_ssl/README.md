# 0x10. HTTPS SSL

-   By Sylvain Kalache, co-founder at Holberton School
-   Ongoing project - started 08-26-2021, must end by 08-27-2021 (in about 5 hours) - you're done with  0% of tasks.
-   Checker was released at 08-26-2021 12:00 PM
-   QA review fully automated.

## Concepts

_For this project, students are expected to look at these concepts:_

-   [DNS](https://intranet.hbtn.io/concepts/12)
-   [Web stack debugging](https://intranet.hbtn.io/concepts/68)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png)

## Background Context

### What happens when you don’t secure your website traffic?

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/xCmOCgw.gif)

## Resources

**Read or watch**:

-   [What is HTTPS?](https://intranet.hbtn.io/rltoken/pawxG_0c1o86psexBOikIw "What is HTTPS?")
-   [What are the 2 main elements that SSL is providing](https://intranet.hbtn.io/rltoken/jXCB9Hn-ALcP78kPMHtnSA "What are the 2 main elements that SSL is providing")
-   [HAProxy SSL termination on Ubuntu16.04](https://intranet.hbtn.io/rltoken/UkbvWfKF6ZAY_CUvlM32lA "HAProxy SSL termination on Ubuntu16.04")
-   [SSL termination](https://intranet.hbtn.io/rltoken/VFq2MQ9qHXw2Nb11tnWF6Q "SSL termination")
-   [Bash function](https://intranet.hbtn.io/rltoken/16bxrQvaOSIywA_fHEdsiA "Bash function")

**man or help**:

-   `awk`
-   `dig`

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/nG-LdAd2DncgHvhnQR4KAw "explain to anyone"),  **without the help of Google**:

### General

-   What is HTTPS SSL 2 main roles
-   What is the purpose encrypting traffic
-   What SSL termination means

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 16.04 LTS
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass  `Shellcheck`  (version  `0.3.7`) without any error
-   The first line of all your Bash scripts should be exactly  `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

## Quiz questions

Show

## Your servers

Name

Username

IP

State

2644-web-01

`ubuntu`

`34.138.245.164`

running

[Soft reboot](https://intranet.hbtn.io/servers/5927/soft_reboot)

[Hard reboot](https://intranet.hbtn.io/servers/5927/hard_reboot)

[Ask a new server](https://intranet.hbtn.io/servers/5927/ask_new)

2644-web-02

`ubuntu`

`54.224.201.40`

running

[Soft reboot](https://intranet.hbtn.io/servers/6301/soft_reboot)

[Hard reboot](https://intranet.hbtn.io/servers/6301/hard_reboot)

[Ask a new server](https://intranet.hbtn.io/servers/6301/ask_new)

2644-lb-01

`ubuntu`

`54.152.39.84`

running

[Soft reboot](https://intranet.hbtn.io/servers/6486/soft_reboot)

[Hard reboot](https://intranet.hbtn.io/servers/6486/hard_reboot)

Last: [Ask a new server](https://intranet.hbtn.io/servers/6486/ask_new)

## Tasks

### 0. World wide web

mandatory

Configure your domain zone so that the subdomain  `www`  points to your load-balancer IP (`lb-01`). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

Requirements:

-   Add the subdomain  `www`  to your domain, point it to your  `lb-01`  IP (your domain name might be configured with default subdomains, feel free to remove them)
-   Add the subdomain  `lb-01`  to your domain, point it to your  `lb-01`  IP
-   Add the subdomain  `web-01`  to your domain, point it to your  `web-01`  IP
-   Add the subdomain  `web-02`  to your domain, point it to your  `web-02`  IP
-   Your Bash script must accept 2 arguments:
    1.  `domain`:
        -   type: string
        -   what: domain name to audit
        -   mandatory: yes
    2.  `subdomain`:
        -   type: string
        -   what: specific subdomain to audit
        -   mandatory: no
-   Output:  `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
-   When only the parameter  `domain`  is provided, display information for its subdomains  `www`,  `lb-01`,  `web-01`  and  `web-02`  - in this specific order
-   When passing  `domain`  and  `subdomain`  parameters, display information for the specified subdomain
-   Ignore  `shellcheck`  case  `SC2086`
-   Must use:
    -   `awk`
    -   at least one Bash function
-   You do not need to handle edge cases such as:
    -   Empty parameters
    -   Nonexistent domain names
    -   Nonexistent subdomains

Example:

```
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x10-https_ssl`
-   File:  `0-world_wide_web`

Done?  Help  Check your code  Get a sandbox

### 1. HAproxy SSL termination

mandatory

“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using  `certbot`  and configure  `HAproxy`  to accept encrypted traffic for your subdomain  `www.`.

Requirements:

-   HAproxy must be listening on port TCP 443
-   HAproxy must be accepting SSL traffic
-   HAproxy must serve encrypted traffic that will return the  `/`  of your web server
-   When querying the root of your domain name, the page returned must contain  `Holberton School`
-   Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`)

The file  `1-haproxy_ssl_termination`  must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher,  [SSL termination](https://intranet.hbtn.io/rltoken/VFq2MQ9qHXw2Nb11tnWF6Q "SSL termination")  is not available before v1.5.

Example:

```
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x10-https_ssl`
-   File:  `1-haproxy_ssl_termination`
