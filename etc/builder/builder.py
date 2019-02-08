#!/usr/bin/env python3

from random import uniform
import jinja2
import argparse
import os

def write_config(tmpl, conf_dir, label, port, server, n_bytes, bandwidth):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))
    output = env.get_template(tmpl).render(label=label, port=port, server= server, n_bytes= n_bytes, bandwidth= bandwidth, indent=4*" ")
    with open(os.path.join(conf_dir, label + ".yaml"), "w") as fh:
        fh.write(output)

def make_at_points(num_at_points, distance):
    # Pick a random point in [0, distance-1] (with decisecond precision)
    t0 = float("{:.1f}".format(uniform(0, distance - 1)))

    # Place as many points as requested at distance "distance" starting at t0
    return [t0 + offset for offset in range(0, num_at_points * distance, distance)]

def main():
    parser = argparse.ArgumentParser(description="create trafic configuration files from a template")
    parser.add_argument("--port", required=False, type=int, help="port")
    parser.add_argument("--dest_dir", required=False, type=str, help="folder where to store the produced configuration files")
    # ~ parser.add_argument("--num_files", required=False, type=int, help="number of files to create")
    parser.add_argument("--label", required=False, type=str, help="a label for the traffic flow (also the basename for the produced file)")
    parser.add_argument("--template", required=False, type=str, help="the template file name")
    # ~ parser.add_argument("--num_at_points", required=False, type=int, help="number of 'at' points to produce")
    # ~ parser.add_argument("--at_points_distance", required=False, type=int, help="distance (in seconds) between 'at' points")
    parser.add_argument("--bandwidth", required=False, type=str, help="Desired bandwith consuption")
    parser.add_argument("--server", required=False, type=str, help="IPv4 address of the server")
    parser.add_argument("--n_bytes", required=False, type=str, help="Number of bytes to be sent")
    

    args = parser.parse_args()

    port = args.port
    label = "%s-%d" % (args.label, port)
    # ~ at_points = make_at_points(args.num_at_points, args.at_points_distance)
    server = "%s" % (args.server)
    bandwidth = "%s" % (args.bandwidth)
    n_bytes = "%s" % (args.n_bytes)
    
    print(server)

    write_config(args.template, args.dest_dir, label, port, server, n_bytes, bandwidth, )

if __name__ == "__main__":
    main()
