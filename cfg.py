import consorts

cmd_prefix = "!"
cmd_thrash = cmd_prefix + "thrash"
cmd_doublethrash = cmd_prefix + "doublethrash"
cmd_triplethrash = cmd_prefix + "triplethrash"
cmd_quadruplethrash = cmd_prefix + "quadruplethrash"
cmd_quadruplethrash_alt1 = cmd_prefix + "quadthrash"
cmd_quintuplethrash = cmd_prefix + "quintuplethrash"
cmd_quintuplethrash_alt1 = cmd_prefix + "quinthrash"
cmd_sextuplethrash = cmd_prefix + "sextuplethrash"
cmd_sextuplethrash_alt1 = cmd_prefix + "sexthrash"
cmd_septuplethrash = cmd_prefix + "septuplethrash"
cmd_septuplethrash_alt1 = cmd_prefix + "septhrash"
cmd_takedown = cmd_prefix + "takedown"
cmd_themes = cmd_prefix + "themes"
cmd_gamering = cmd_prefix + "gamering"
cmd_frog = cmd_prefix + "frog"
cmd_goodboy = cmd_prefix + "goodboy"
cmd_laughtrack = cmd_prefix + "laughtrack"
cmd_modelo = cmd_prefix + "modelo"
cmd_vibecheck = cmd_prefix + "vibecheck"
cmd_thrashcoin = cmd_prefix + "thrashcoin"
cmd_thrashcoin_alt1 = cmd_prefix + "tc"
cmd_thrashcoin_alt2 = cmd_prefix + "coin"
cmd_leaderboard = cmd_prefix + "leaderboard"

col_id_user = "id_user"
col_thrashcoin = "thrashcoin"

emote_rf = "<:rf:583865629350559744>"
emote_s1 = "<:s1:583866803047104563>"
emote_s3 = "<:s3:583866847451938831>"
emote_blank = "<:blank:637402727810596874>"
emote_munchy = "<:munchy:489611810102575114>"
emote_etlaugh = "<:etlaugh:642844353282441231>"

booru_commands = {
    cmd_prefix + "doop": consorts.doop,
    cmd_prefix + "kan": consorts.kanman,
    cmd_prefix + "crocs": consorts.crocs,
    cmd_prefix + "paradox": consorts.crocs,
    cmd_prefix + "sixt": consorts.sixten,
    cmd_prefix + "juan": consorts.juan,
    cmd_prefix + "nnoby": consorts.nnoby,
    cmd_prefix + "conn": consorts.connor,
    cmd_prefix + "niboe": consorts.niboe,
    cmd_prefix + "sean": consorts.scythe,
    cmd_prefix + "scythe": consorts.scythe,
    cmd_prefix + "noone": consorts.frog,
    cmd_prefix + "lat": consorts.lateralyst,
    cmd_prefix + "fat": consorts.fat,
    cmd_prefix + "yoshi": consorts.fat,
    cmd_prefix + "hex": consorts.hex,
    cmd_prefix + "robo": consorts.robo,
    cmd_prefix + "krip": consorts.krip,
    cmd_prefix + "king": consorts.krip,
    cmd_prefix + "ed": consorts.krip,
    cmd_prefix + "rosa": consorts.krip,
    cmd_prefix + "m@": consorts.m,
    cmd_prefix + "mat": consorts.m,
    cmd_prefix + "shill": consorts.m,
    cmd_prefix + "kof": consorts.koff,
    cmd_prefix + "kab": consorts.kab,
    cmd_prefix + "jane": consorts.kab,
    cmd_prefix + "mal": consorts.mal,
    cmd_prefix + "sweet": consorts.mal,
    cmd_prefix + "mouse": consorts.mal,
    cmd_prefix + "mill": consorts.miller,
    cmd_prefix + "bluem": consorts.miller,
    cmd_prefix + "manson": consorts.miller,
    cmd_prefix + "meaty": consorts.meaty,
    cmd_prefix + "ethan": consorts.ethan,
    cmd_prefix + "straub": consorts.ethan,
    cmd_prefix + "munch": consorts.munchy,
    cmd_prefix + "stotle": consorts.stotle,
    cmd_prefix + "aris": consorts.stotle,
    cmd_prefix + "kib": consorts.kibun,
    cmd_prefix + "gab": consorts.gabe,
    cmd_prefix + "scep": consorts.sceptrai,
    cmd_prefix + "omni": consorts.omni,
    cmd_prefix + "fork": consorts.forkes,
    cmd_prefix + "shad": consorts.shadok,
    cmd_prefix + "cal": consorts.callum,
    cmd_prefix + "pris": consorts.prism,
    cmd_prefix + "ack": consorts.ackro,
    cmd_prefix + "smear": consorts.smearg,
}

client_ref = None

def get_client():
	global client_ref
	return client_ref;

"""
	save the discord client of this bot
"""
def set_client(cl):
	global client_ref
	client_ref = cl

	return client_ref