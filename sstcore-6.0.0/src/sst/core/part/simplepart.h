// Copyright 2009-2016 Sandia Corporation. Under the terms
// of Contract DE-AC04-94AL85000 with Sandia Corporation, the U.S.
// Government retains certain rights in this software.
// 
// Copyright (c) 2009-2016, Sandia Corporation
// All rights reserved.
// 
// This file is part of the SST software package. For license
// information, see the LICENSE file in the top level directory of the
// distribution.
#ifndef SST_CORE_PART_SIMPLEPART_H
#define SST_CORE_PART_SIMPLEPART_H

#include "sst/core/part/sstpart.h"

namespace SST {
namespace Partition{
    
class SimplePartitioner : public SST::Partition::SSTPartitioner {

private:
    RankInfo world_size;
    static bool initialized;
    
public:
    
    SimplePartitioner(RankInfo total_ranks);
    SimplePartitioner();
    ~SimplePartitioner() {}

    void performPartition(PartitionGraph* graph);

    bool requiresConfigGraph() { return false; }
    bool spawnOnAllRanks() { return false; }

    static SSTPartitioner* allocate(RankInfo total_ranks, RankInfo my_rank, int verbosity) {
        return new SimplePartitioner(total_ranks);
    }

};

} // namespace partition
} //namespace SST
#endif //SST_CORE_PART_SIMPLERPART_H
