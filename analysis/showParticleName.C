void showParticleName(
    TString file_path = "/home/tomoe/mc/bench/test0.root"
){
    
    // read root files
    TChain* chain = new TChain("tree");
    chain->Add(file_path);

    // output read files
    TObjArray *fileElements = chain->GetListOfFiles();
    TIter next(fileElements);
    TChainElement *chEl = 0;
    while (( chEl=(TChainElement*)next() )) {
        fprintf(stdout, "read\t'%s'\n", chEl->GetTitle());
    }

    // init TTreeReader instead of SetBranchAddress
    TTreeReader reader(chain);
    TTreeReaderValue<int> nHit(reader, "nHit");
    TTreeReaderArray<int> particleID(reader, "particle");

    // m_particles = {pdgcode: number of particles}
    map<int, int> n_particles;

    // count number of particles
    while(reader.Next()){
        if (*nHit == 0) continue;
        set<int> particleID_unique(particleID.begin(), particleID.end());
        for (auto itr = particleID_unique.begin(); itr != particleID_unique.end(); ++itr){
            if (n_particles.count(*itr) == 0){
                n_particles[*itr] = 1;
            } else {
                n_particles[*itr] += 1;
            }
        }
    }

    // output count results while convert PDGcode into particle name
    TDatabasePDG* pdg = new TDatabasePDG();
    for (auto itr = n_particles.begin(); itr != n_particles.end(); ++itr){
        if (itr->first > 1000000000) continue;
        cout << pdg->GetParticle(itr->first)->GetName() << "\t" << itr->second << endl;
    }

}