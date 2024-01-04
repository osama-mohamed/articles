@echo off
title restart_odoo_script

docker restart odoo17

docker exec odoo17 odoo -c /etc/odoo/odoo.conf -d odoo -u it_courses
