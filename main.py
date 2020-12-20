import module



if __name__ == '__main__':
    addpromoter = module.PromoterUpdater()
    
    if addpromoter.promoterupdate():
        checkpromoter = module.PromoterChecker()
        checkpromoter.promotercheck()