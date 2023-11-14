import sqlite3
import csv

def charge_blade_dbs():
    connection_obj_4 = sqlite3.connect('hitzones.db')
    cursor_obj_4 = connection_obj_4.cursor()
    cursor_obj_4.execute("DROP TABLE IF EXISTS HITZONES")
    hitzones_table = """ 
                       CREATE TABLE HITZONES (
                       name CHAR(255) NOT NULL,
                       part CHAR(25) NOT NULL,
                       cut INT,
                       caff INT,
                       blunt INT,
                       baff INT,
                       pierce INT,
                       paff INT,
                       fire_def INT,
                       fexp INT,
                       water_def INT,
                       wexp INT,
                       ice_def INT,
                       iexp INT,
                       thunder_def INT,
                       texp INT,
                       dragon_def INT,
                       dexp INT,
                       ko INT
                       );
                   """
    cursor_obj_4.execute(hitzones_table)
    print('Hitzones Table is ready')
    connection_obj_4.close()

    connection_obj = sqlite3.connect('weapon.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("DROP TABLE IF EXISTS WEAPON")
    weapon_table = """ 
            CREATE TABLE WEAPON (
            name CHAR(255) NOT NULL,
            weapon_type CHAR(25) NOT NULL,
            raw_attack INT,
            affinity INT,
            element INT,
            status INT,
            type CHAR(25) NOT NULL,
            sub_type CHAR(25) NOT NULL,
            sharpness INT,
            esharpness INT,
            slots CHAR(5) NOT NULL,
            rampage_slot INT,
            sharpness_upgrade INT,
            purple_sharpness INT,
            white_sharpness INT,
            blue_sharpness INT
            );
        """
    cursor_obj.execute(weapon_table)
    print('Weapon Table is ready')
    connection_obj.close()

    connection_obj_5 = sqlite3.connect('motion.db')
    cursor_obj_5 = connection_obj_5.cursor()
    cursor_obj_5.execute("DROP TABLE IF EXISTS MOTION")
    motion_table = """ 
               CREATE TABLE MOTION (
               weapon CHAR (25) NOT NULL,
               move_name CHAR(255) NOT NULL,
               damage_type NOT NULL,
               raw INT,
               element INT, 
               status INT,
               part_continue INT,
               stun INT, 
               exhaust INT,
               mount INT,
               misc INT
               );
           """
    cursor_obj_5.execute(motion_table)
    print('Motion Table is ready')
    connection_obj_5.close()

    connection_obj_3 = sqlite3.connect('hitzones.db')
    cursor_obj_3 = connection_obj_3.cursor()
    with open("hitzones.csv", 'r') as file:
        csvreader_3 = csv.reader(file)
        for row3 in csvreader_3:
            print(row3)
            name = row3[0]
            part = row3[1]
            cut = row3[2]
            caff = row3[3]
            blunt = row3[4]
            baff = row3[5]
            pierce = row3[6]
            paff = row3[7]
            fire_def = row3[8]
            fexp = row3[9]
            water_def = row3[10]
            wexp = row3[11]
            ice_def = row3[12]
            iexp = row3[13]
            thunder_def = row3[14]
            texp = row3[15]
            dragon_def = row3[16]
            dexp = row3[17]
            ko = row3[18]
            cursor_obj_3.execute("INSERT INTO hitzones (""name, part, cut, caff, blunt, baff, pierce, paff, fire_def, fexp,"
                                 "water_def, wexp, ice_def, iexp, thunder_def, texp, dragon_def, dexp, ko)"
                                 "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                 (name, part, cut, caff, blunt, baff, pierce, paff, fire_def, fexp,
                                 water_def, wexp, ice_def, iexp, thunder_def, texp, dragon_def, dexp, ko))
    connection_obj_3.commit()
    connection_obj_3.close()

    connection_obj = sqlite3.connect('weapon.db')
    cursor_obj = connection_obj.cursor()
    with open("weapon.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row1 in csvreader:
            print(row1)
            name = row1[0]
            weapon_type = row1[1]
            raw_attack = row1[2]
            affinity = row1[3]
            element = row1[4]
            status = row1[5]
            element_type = row1[6]
            sub_type = row1[7]
            sharpness = row1[8]
            esharpness = row1[9]
            slots = row1[10]
            rampage_slots = row1[11]
            sharpness_upgrade = row1[12]
            purple = row1[13]
            white = row1[14]
            blue = row1[15]
            cursor_obj.execute("INSERT INTO weapon (""name, weapon_type, raw_attack, affinity, element, status,"
                               "type, sub_type, sharpness, esharpness, slots, rampage_slot, sharpness_upgrade, purple_sharpness, "
                               "white_sharpness, blue_sharpness)"
                               "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                               (name, weapon_type, raw_attack, affinity, element, status,
                                element_type, sub_type, sharpness, esharpness, slots, rampage_slots, sharpness_upgrade,
                                purple, white, blue))
    connection_obj.commit()
    connection_obj.close()

    connection_obj_2 = sqlite3.connect('motion.db')
    cursor_obj_2 = connection_obj_2.cursor()
    with open("motions.csv", 'r') as file:
        csvreader_2 = csv.reader(file)
        for row2 in csvreader_2:
            print(row2)
            weapon = row2[0]
            move_name = row2[1]
            damage_type = row2[2]
            raw = row2[3]
            element = row2[4]
            status = row2[5]
            part_continue = row2[6]
            stun = row2[7]
            exhaust = row2[8]
            mount = row2[9]
            misc = row2[10]
            cursor_obj_2.execute("INSERT INTO motion (""weapon, move_name, damage_type, raw, element, status,"
                               "part_continue, stun, exhaust, mount, misc)"
                               "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                               (weapon, move_name, damage_type, raw, element, status,
                                part_continue, stun, exhaust, mount, misc))
    connection_obj_2.commit()
    connection_obj_2.close()
