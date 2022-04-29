# duckdns
now make the duck.sh file executeable 
```
chmod 700 duck.sh
```
next we will be using the cron process to make the script get run every 5 minutes 
```
crontab -e
```
 copy this text and paste it at the bottom of the crontab 
 ```
*/5 * * * * ~/duckdns/duck.sh >/dev/null 2>&1
```
we can also see if the last attempt was successful (OK or bad KO)
```
cat duck.log
```
