from diagrams import Diagram
from diagrams import Cluster

from diagrams.onprem.container import Docker
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.iac import Ansible

from diagrams.onprem.network import Internet
from diagrams.onprem.network import Traefik

from diagrams.generic.network import Firewall
from diagrams.generic.network import Switch

from diagrams.generic.os import Raspbian
from diagrams.generic.os import Ubuntu
from diagrams.generic.os import Debian

from diagrams.saas.chat import Slack
from diagrams.saas.cdn import Cloudflare


with Diagram("Infrastructure", show=False, filename="diagrams/png/infra_diagram"):
  with Cluster("RPI4-1"):
    with Cluster("Raspbian"):
      rpi4_1 = Raspbian("RPI4-1")

    with Cluster("Docker"):
      with Cluster("Traefik"):
        traefik = Traefik("Traefik")
      with Cluster("PostgreSQL"):
        postgres = PostgreSQL("PostgreSQL")

      with Cluster("Docker"):
        docker = Docker("Docker")