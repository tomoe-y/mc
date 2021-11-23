void showParticleName(
    TString file_path = "/home/tomoe/mc/bench/test0.root"
){
    auto file = new TFile(file_path);
    TTreeReader reader("tree", file);

    TTreeReaderValue<int> nHit(reader, "nHit");
    TTreeReaderArray<int> particleID(reader, "particle");

    map<int, int> n_particles;

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

    TDatabasePDG* pdg = new TDatabasePDG();
    for (auto itr = n_particles.begin(); itr != n_particles.end(); ++itr){
        if (itr->first > 1000000000) continue;
        cout << pdg->GetParticle(itr->first)->GetName() << ": " << itr->second << endl;
    }

}