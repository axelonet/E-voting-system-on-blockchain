import simplejson as json

def jsonify_votedata(votedatalist):
    jsondict = {'public_key': votedatalist[0], 'data':votedatalist[1],'key':votedatalist[2]}
    #--this returns a string for the dictionary but converts the bytes data
    #--into string...so we need to convert it back when recieved on the
    #--other end of the peer....
    return json.dumps(jsondict)

