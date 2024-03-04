from diagrams import Diagram, Cluster

from diagrams.onprem.container.Docker import Docker
from diagrams.onprem.database.postgresql import PostgreSQL
from diagrams.onprem.iac.Ansible import Ansible

from diagrams.onprem.network.Internet import Internet
from diagrams.onprem.network.Traefik import Traefik

from diagrams.generic.network.Firewall import Firewall
from diagrams.generic.network.Switch import Switch

from diagrams.generic.os.Raspbian import Raspbian
from diagrams.generic.os.Ubuntu import Ubuntu
from diagrams.generic.os.Debian import Debian

from diagrams.saas.chat.Slack import Slack
from diagrams.saas.cdn.Cloudflare import Cloudflare


with Diagram("Infrastructure", show=False, filename="png/infra_diagram.png"):
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