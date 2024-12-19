from PyDect200 import PyDect200

PyDect200 = PyDect200.PyDect200


def fritz_dect_on():

    fritz_con = PyDect200('FFW-Rubenheim!?#', username='fritz1026')
    fritz_con.switch_onoff('087610067966',1)


def fritz_dect_off():

    fritz_con = PyDect200('FFW-Rubenheim!?#', username='fritz1026')
    fritz_con.switch_onoff('087610067966',0)