import random

# -------------------------
# Κλάσεις για ΣΔΤ (classification)
# -------------------------

def classify_SDT(x1, x2):
    # 1-4: κύκλος γύρω από (0.5,0.5)
    if (x1 - 0.5) ** 2 + (x2 - 0.5) ** 2 < 0.2:
        if x1 > 0.5 and x2 > 0.5:
            return "C1"  # 1)
        elif x1 < 0.5 and x2 > 0.5:
            return "C2"  # 2)
        elif x1 > 0.5 and x2 < 0.5:
            return "C2"  # 3)
        elif x1 < 0.5 and x2 < 0.5:
            return "C1"  # 4)

    # 5-8: κύκλος γύρω από (1.5,0.5)
    if (x1 - 1.5) ** 2 + (x2 - 0.5) ** 2 < 0.2:
        if x1 > 1.5 and x2 > 0.5:
            return "C1"  # 5)
        elif x1 < 1.5 and x2 > 0.5:
            return "C2"  # 6)
        elif x1 > 1.5 and x2 < 0.5:
            return "C2"  # 7)
        elif x1 < 1.5 and x2 < 0.5:
            return "C1"  # 8)

    # 9-12: κύκλος γύρω από (0.5,1.5)
    if (x1 - 0.5) ** 2 + (x2 - 1.5) ** 2 < 0.2:
        if x1 > 0.5 and x2 > 1.5:
            return "C1"  # 9)
        elif x1 < 0.5 and x2 > 1.5:
            return "C2"  # 10)
        elif x1 > 0.5 and x2 < 1.5:
            return "C2"  # 11)
        elif x1 < 0.5 and x2 < 1.5:
            return "C1"  # 12)

    # 13-16: κύκλος γύρω από (1.5,1.5)
    if (x1 - 1.5) ** 2 + (x2 - 1.5) ** 2 < 0.2:
        if x1 > 1.5 and x2 > 1.5:
            return "C1"  # 13)
        elif x1 < 1.5 and x2 > 1.5:
            return "C2"  # 14)
        elif x1 > 1.5 and x2 < 1.5:
            return "C2"  # 15)
        elif x1 < 1.5 and x2 < 1.5:
            return "C1"  # 16)

    # 17-18: έξω από τους κύκλους
    prod = (x1 - 1.0) * (x2 - 1.0)
    if prod > 0:
        return "C3"  # 17)
    elif prod < 0:
        return "C4"  # 18)
    else:
        # αν είναι ακριβώς πάνω σε x1=1 ή x2=1 (σχεδόν ποτέ)
        return "C3"


def generate_SDT_files():
    N_total = 8000
    points = []

    for _ in range(N_total):
        x1 = random.uniform(0.0, 2.0)
        x2 = random.uniform(0.0, 2.0)
        cls = classify_SDT(x1, x2)
        points.append((x1, x2, cls))

    train = points[:4000]
    test = points[4000:]

    # Γραμμή header (την αγνοεί το πρόγραμμα σου με το πρώτο fgets)
    header = "x1,x2,class\n"

    # Μορφή γραμμής που περιμένει το make_pair:
    # x1,x2, C1
    def format_line(x1, x2, cls):
        return f"{x1:.6f},{x2:.6f}, {cls}\n"

    with open("trainingData.csv", "w") as f_train:
        f_train.write(header)
        for x1, x2, cls in train:
            f_train.write(format_line(x1, x2, cls))

    with open("checkData.csv", "w") as f_test:
        f_test.write(header)
        for x1, x2, cls in test:
            f_test.write(format_line(x1, x2, cls))

    print("Έφτιαξα trainingData.csv και checkData.csv για το MLP σου.")


# -------------------------
# ΣΔΟ: ομαδοποίηση (SDO.txt)
# -------------------------

def generate_SDO_file():
    points = []

    # 1) 150 σημεία στο [0.75,1.25]x[0.75,1.25]
    for _ in range(150):
        x1 = random.uniform(0.75, 1.25)
        x2 = random.uniform(0.75, 1.25)
        points.append((x1, x2))

    # 2) 150 σημεία στο [0,0.5]x[0,0.5]
    for _ in range(150):
        x1 = random.uniform(0.0, 0.5)
        x2 = random.uniform(0.0, 0.5)
        points.append((x1, x2))

    # 3) 150 σημεία στο [0,0.5]x[1.5,2]
    for _ in range(150):
        x1 = random.uniform(0.0, 0.5)
        x2 = random.uniform(1.5, 2.0)
        points.append((x1, x2))

    # 4) 150 σημεία στο [1.5,2]x[0,0.5]
    for _ in range(150):
        x1 = random.uniform(1.5, 2.0)
        x2 = random.uniform(0.0, 0.5)
        points.append((x1, x2))

    # 5) 150 σημεία στο [1.5,2]x[1.5,2]
    for _ in range(150):
        x1 = random.uniform(1.5, 2.0)
        x2 = random.uniform(1.5, 2.0)
        points.append((x1, x2))

    # 6) 75 σημεία στο [0.6,0.8]x[0,0.4]
    for _ in range(75):
        x1 = random.uniform(0.6, 0.8)
        x2 = random.uniform(0.0, 0.4)
        points.append((x1, x2))

    # 7) 75 σημεία στο [0.6,0.8]x[1.6,2]
    for _ in range(75):
        x1 = random.uniform(0.6, 0.8)
        x2 = random.uniform(1.6, 2.0)
        points.append((x1, x2))

    # 8) 75 σημεία στο [1.2,1.4]x[0,0.4]
    for _ in range(75):
        x1 = random.uniform(1.2, 1.4)
        x2 = random.uniform(0.0, 0.4)
        points.append((x1, x2))

    # 9) 75 σημεία στο [1.2,1.4]x[1.6,2]
    for _ in range(75):
        x1 = random.uniform(1.2, 1.4)
        x2 = random.uniform(1.6, 2.0)
        points.append((x1, x2))

    # 10) 150 σημεία στο [0,2]x[0,2]
    for _ in range(150):
        x1 = random.uniform(0.0, 2.0)
        x2 = random.uniform(0.0, 2.0)
        points.append((x1, x2))

    print("Σύνολο ΣΔΟ:", len(points))  # πρέπει να είναι 1200

    # Υποθέτω ότι το πρόγραμμα ομαδοποίησης διαβάζει "x1 x2" ανά γραμμή
    with open("SDO.txt", "w") as f:
        for x1, x2 in points:
            f.write(f"{x1:.6f} {x2:.6f}\n")

    print("Έφτιαξα SDO.txt για το k-means.")


if __name__ == "__main__":
    print("Δημιουργία δεδομένων για ΣΔΤ & ΣΔΟ...")
    generate_SDT_files()
    generate_SDO_file()
    print("Τέλος.")
