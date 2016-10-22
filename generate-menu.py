import sys
import csv
import apriori

attribs_map = {}
case_votes = {}

log_file = sys.argv[1]

with open(log_file) as f:
    reader = csv.reader(f, delimiter=",")
    current_case_id = None
    for row in reader:
        line_type = row[0]
        if line_type == 'A':  # attribute line
            attr_id = row[1]
            attr_name = row[3]
            attr_path = row[4]
            entry = {"name": attr_name, "path": attr_path}
            attribs_map[attr_id] = entry
        if line_type == 'C':  # case line
            case_id = row[1]
            current_case_id = case_id
            case_votes[case_id] = set()
        if line_type == 'V':  # vote line
            item_id = row[1]
            case_votes[current_case_id].add(item_id)


dataset = []
for k,v in case_votes.iteritems():
    # print k,v
    basket = map(lambda a: attribs_map[a]['path'], v)
    dataset.append(basket)

## Generate rules
L, support_data = apriori.apriori(dataset,minsupport=0.01)
apriori.generateRules(L, support_data)
retlist = apriori.generateRules(L, support_data, min_confidence=0.5)


print "Rules:"
for rule in retlist:
    lhs, rhs, confidence = rule
    percent = confidence * 100
    lhs = list(lhs)
    rhs = list(rhs)
    print "%.4f %% chance that: %s => %s" % (percent, ",".join(lhs), ",".join(rhs))

