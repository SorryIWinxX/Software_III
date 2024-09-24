#!/bin/bash

# Ruta del script Ruby
ruby_script_1="publisher-1.rb"
ruby_script_2="publisher-2.rb"

# Bucle infinito para ejecutar el script cada 3 segundos
while true; do
  ruby "$ruby_script_1"
  ruby "$ruby_script_2"
  sleep 3
done
