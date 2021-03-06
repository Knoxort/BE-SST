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


#include <sst_config.h>
#include "zcomputeevent.h"

using namespace SST::Hermes;
using namespace SST::Zodiac;
using namespace SST;

ZodiacComputeEvent::ZodiacComputeEvent(double time) {
	computeTime = time;
}

ZodiacEventType ZodiacComputeEvent::getEventType() {
	return Z_COMPUTE;
}

double ZodiacComputeEvent::getComputeDuration() {
	return computeTime;
}

double ZodiacComputeEvent::getComputeDurationNano() {
	return computeTime * 1000000000.0;
}
