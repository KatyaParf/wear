import sys
import operator
import array
import os
from subprocess import PIPE, Popen


def recommend(cur_temp, cur_osad):
    curdir = os.getcwd()
    log.debug("-- recommend -- " + curdir)
    log.debug("-- recommend -- t = " + cur_temp)
    log.debug("-- recommend -- osad = " + cur_osad)

    # TODO
    cur_osad = str( 1 )

    cmd = "what_to_wear_main.py " + cur_temp + " " + cur_osad
    if (curdir == "/config"):
        cmd = "/config/pyscript/" + cmd
    p = Popen("python3 " + cmd, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()

    res = stdout.decode('utf-8')
    log.debug("-- recommend -- res = " + res)

    res_err = stderr.decode('utf-8')
    log.debug("-- recommend -- err = " + res_err)

    return res


#@service
def what_to_wear():
    cur_temp = str( state.get("weather.home.temperature") )
    cur_osad = str( state.get("weather.home") )

    res = recommend(cur_temp, cur_osad)

    # use dialog because long text
    media_player.play_media(
        entity_id = "media_player.yandex_station_bedroom",
        media_content_type = "dialog",
        media_content_id = res
    )

    # say comma to stop dialog
    #media_player.play_media(
    #    entity_id = "media_player.yandex_station_bedroom",
    #    media_content_type = "text",
    #    media_content_id = ". Удачи! "
    #)

#------------------

def main(argv):
    sredTemp = int(float(sys.argv[1]))
    sredOsad = int(sys.argv[2])

    res = recommend(sredTemp, sredOsad)
    print(res)


#-----------

if __name__ == "__main__":
    main(sys.argv)