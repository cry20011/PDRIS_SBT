# PDRIS_SBT

Поднял три сервера на VirtualBox
- Ansible: 192.168.56.101
- Servers: 192.168.56.102, 192.168.56.103

Playbook:
Запулил image back из первой лабы с исходниками, и создал ещё один где настраиваются среды, то есть устанавливаются requirements.txt.
Далее получаю с помощью volume исходники, и передаю готовый артифакт в чистый контейнер с настроенными средами.

Запустив на ansible сервере `ansible-playbook docker_images_build.yml`, перейдя на соответствующие хосты получил

![](https://github.com/cry20011/PDRIS_SBT/blob/lab2/image_2022-11-04_17-52-41.png)
