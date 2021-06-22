jordan_belfort = {"calls": 178, "meetings":17, "sales":6}
beldan_jorfort = {"calls": 121, "meetings":32, "sales":8}


def calc_score(dict):
    try:
        dict["score"] = dict["calls"] * 10
        dict["score"] += dict["meetings"] * 30
        dict["score"] += dict["sales"] * 100
        if dict["calls"] > 150:
            dict["score"] += 100
        if dict["meetings"] > 20:
            dict["score"] += 100
        if dict["sales"] > 5:
            dict["score"] += 100
        
        return dict

    except Exception as e:
        return (f"Error: {e}")

print(calc_score(jordan_belfort))
print(calc_score(beldan_jorfort))
