{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.11";
    nixpkgs-unstable.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
    nixpkgs-unstable,
    ...
  }: let
    systems = [
      "x86_64-linux"
      "aarch64-linux"
      "x86_64-darwin"
      "aarch64-darwin"
    ];
    overlay-unstable = final: prev: {
      unstable = nixpkgs-unstable.legacyPackages.${prev.system};
    };

    forAllSystems = nixpkgs.lib.genAttrs systems;
  in {
    devShells = forAllSystems (
      system: let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [overlay-unstable];
        };
      in {
        default = pkgs.mkShell {
          packages = with pkgs; [
            unstable.bootdev-cli
            uv
            python312
          ];
        };
      }
    );
  };
}
