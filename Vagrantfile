# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "box-cutter/centos70"
  config.vm.box_check_update = false
  config.vm.synced_folder "./", "/vagrant", disabled: true

  # nginx ------------------------------------------------------------------
  config.vm.define "nginx.devops.com", primary: true do |node|
    node.vm.host_name = "nginx.devops.com"
    node.vm.network "private_network", ip: "10.127.0.10"
    node.vm.provider "virtualbox" do |vb|
        vb.memory = "512"
        vb.cpus = 2
    end

    node.vm.provision "ansible" do |ansible|
     ansible.playbook = "provision/nginx/nginx.yml"
     ansible.inventory_path = "provision/hosts"
     ansible.limit = "nginx"
     ansible.verbose = "v"
    end
  end
  # ------------------------------------------------------------------------

  # php --------------------------------------------------------------------
  config.vm.define 'php.devops.com' do |node|
    node.vm.host_name = 'php.devops.com'
    node.vm.network "private_network", ip: '10.127.0.20'
    node.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
        vb.cpus = 1
    end

    node.vm.provision "ansible" do |ansible|
     ansible.playbook = "provision/php/php.yml"
     ansible.inventory_path = "provision/hosts"
     ansible.limit = "php"
     ansible.verbose = "v"
    end
  end

  # redis -------------------------------------------------------------------
  config.vm.define 'redis.devops.com' do |node|
    node.vm.host_name = 'redis.devops.com'
    node.vm.network "private_network", ip: '10.127.0.30'
    node.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
        vb.cpus = 1
    end

    node.vm.provision "ansible" do |ansible|
     ansible.playbook = "provision/redis/redis.yml"
     ansible.inventory_path = "provision/hosts"
     ansible.limit = "redis"
     ansible.verbose = "v"
    end
  end
  #------------------------------------------------------------------------

  # monitor ---------------------------------------------------------------
  config.vm.define 'monitor.devops.com' do |node|
    node.vm.host_name = 'monitor.devops.com'
    node.vm.network "private_network", ip: '10.127.0.40'
    node.vm.provider "virtualbox" do |vb|
        vb.memory = "256"
        vb.cpus = 1
    end

    node.vm.provision "ansible" do |ansible|
     ansible.playbook = "provision/monitor/monitor.yml"
     ansible.inventory_path = "provision/hosts"
     ansible.limit = "monitor"
     ansible.verbose = "v"
    end
  end
  #------------------------------------------------------------------------
end
