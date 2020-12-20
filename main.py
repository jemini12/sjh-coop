import module



if __name__ == '__main__':
    addpromoter = module.PromoterUpdater()
    
    if addpromoter.promoterupdate():
        checkpromoter = module.PromoterChecker()
        if checkpromoter.promotercheck():
            countpromoter = module.PromoterCounter()
            countpromoter.promotercount()