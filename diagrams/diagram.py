from diagrams import Diagram
from diagrams import Cluster

from diagrams.onprem.container import Docker
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.iac import Ansible

from diagrams.onprem.network import Internet
from diagrams.onprem.network import Traefik
from diagrams.generic.network import Firewall
from diagrams.generic.network import Switch

from diagrams.generic.compute import Rack as generic

from diagrams.generic.os import Raspbian as hyperhdr
from diagrams.generic.os import Debian
from diagrams.generic.os import Ubuntu as rpi41

from diagrams.saas.chat import Slack
from diagrams.saas.cdn import Cloudflare


with Diagram("", show=False, filename="diagrams/png/infra_diagram", direction="TB"):
  with Cluster("Infrastructure"):
    with Cluster("Network"):
      Internet = Internet("Internet") >> Firewall("Firewall") >> Switch("Switch")
    with Cluster(""):
      Slack("Notifications")
      Ansible("Deployment & IAC")

  with Cluster("Services"):
    with Cluster("HyperHDR"):
      hyperhdr = hyperhdr()
      Docker("Docker")
    with Cluster("RPI4-1", direction="LR"):
      rpi41 = rpi41()
      Docker("Docker")
      with Cluster("Containers"):
        Traefik("Traefik")
        PostgreSQL("PostgreSQL") - generic("Gatus")

