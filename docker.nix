{ pkgs ? import <nixpkgs> {} }:

let deps = python-packages: with python-packages; [
  flask
  gunicorn
];
in pkgs.dockerTools.buildImage {
  name = "sigfigs";
  tag = "latest";
  created = "now";

  contents = with pkgs; [
    busybox
    bash
    (python3.withPackages deps)
    ./web
  ];

  config = {
    Cmd = [ "gunicorn" "-b" "0.0.0.0:8080" "sigfigs:app" ];
    ExposedPorts = {
      "8080" = {};
    };
  };
}
