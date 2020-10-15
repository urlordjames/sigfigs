{ pkgs ? import <nixpkgs> {} }:
let dependancies = python-packages: with python-packages; [
  flask
  gunicorn
];
in pkgs.mkShell {
  buildInputs = with pkgs; [
    (python3.withPackages dependancies)
  ];
}
