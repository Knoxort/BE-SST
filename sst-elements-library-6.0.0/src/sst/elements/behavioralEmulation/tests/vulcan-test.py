from cartesianrank import CartesianGrid 

global cartesianData

cartesianData = CartesianGrid(32, 32, 16)

Component( "BGQ-core" )
Program( "BGQ-core", "memory-test.txt" )

Property( "BGQ-core", "app.elementSize", lambda gid, cid, cids, index: 20 )
Property( "BGQ-core", "app.elementsPerProcess", lambda gid, cid, cids, index: 100 )
Property( "BGQ-core", "app.transferSizeX", lambda gid, cid, cids, index: 32768 ) 
Property( "BGQ-core", "app.transferSizeY", lambda gid, cid, cids, index: 32768 )
Property( "BGQ-core", "app.transferSizeZ", lambda gid, cid, cids, index: 65536 )
Property( "BGQ-core", "app.timesteps", lambda gid, cid, cids, index: 1 )
Property( "BGQ-core", "app.phyParam", lambda gid, cid, cids, index: 5 )

Property( "BGQ-core", "mpi.commRank", lambda gid, cid, cids, index: cid  )
Property( "BGQ-core", "mpi.commSize", lambda gid, cid, cids, index: cids )
def cartX(g, rank, c, i): return cartesianData.myCoordinates(rank, "X")
def cartY(g, rank, c, i): return cartesianData.myCoordinates(rank, "Y")
def cartZ(g, rank, c, i): return cartesianData.myCoordinates(rank, "Z")
def cartXp(g, rank, c, i): return cartesianData.neighbourRank(rank, "Xplus")
def cartHasXp(g, rank, c, i): return cartesianData.neighbourRank(rank, "Xplus") >= 0
def cartYp(g, rank, c, i): return cartesianData.neighbourRank(rank, "Yplus")
def cartHasYp(g, rank, c, i): return cartesianData.neighbourRank(rank, "Yplus") >= 0
def cartZp(g, rank, c, i): return cartesianData.neighbourRank(rank, "Zplus")
def cartHasZp(g, rank, c, i): return cartesianData.neighbourRank(rank, "Zplus") >= 0
def cartXm(g, rank, c, i): return cartesianData.neighbourRank(rank, "Xminus")
def cartHasXm(g, rank, c, i): return cartesianData.neighbourRank(rank, "Xminus") >= 0
def cartYm(g, rank, c, i): return cartesianData.neighbourRank(rank, "Yminus")
def cartHasYm(g, rank, c, i): return cartesianData.neighbourRank(rank, "Yminus") >= 0
def cartZm(g, rank, c, i): return cartesianData.neighbourRank(rank, "Zminus")
def cartHasZm(g, rank, c, i): return cartesianData.neighbourRank(rank, "Zminus") >= 0
Property( "BGQ-core", "mpi.cartesianX", cartX )
Property( "BGQ-core", "mpi.cartesianY", cartY )
Property( "BGQ-core", "mpi.cartesianZ", cartZ )
Property( "BGQ-core", "mpi.cartesianXplus", cartXp )
Property( "BGQ-core", "mpi.cartesianHasXplus", cartHasXp )
Property( "BGQ-core", "mpi.cartesianYplus", cartYp )
Property( "BGQ-core", "mpi.cartesianHasYplus", cartHasYp )
Property( "BGQ-core", "mpi.cartesianZplus", cartZp )
Property( "BGQ-core", "mpi.cartesianHasZplus", cartHasZp )
Property( "BGQ-core", "mpi.cartesianXminus", cartXm )
Property( "BGQ-core", "mpi.cartesianHasXminus", cartHasXm )
Property( "BGQ-core", "mpi.cartesianYminus", cartYm )
Property( "BGQ-core", "mpi.cartesianHasYminus", cartHasYm )
Property( "BGQ-core", "mpi.cartesianZminus", cartZm )
Property( "BGQ-core", "mpi.cartesianHasZminus", cartHasZm )
Ordinal( "BGQ-core", "mpi.commRank" )

Relation( "BGQ-core", "BGQ-core", "cpu", "self" )

Attribute( "BGQ-core", "usage", 0.0 )

Operation( "BGQ-core", "wait", NoLookup, None,
           RecvWait(True))
Operation( "BGQ-core", "unwait", NoLookup, None,
           Recv(True))

Operation( "BGQ-core", "computeA", "computeA.csv", "linear",
           Loiter( "usage", "==", 0.0),
           Modify( "usage", 1.0 ),
           Dawdle( Outputs(0) ),
           Modify( "usage", 0.0 ) )
Operation( "BGQ-core", "computeB", "computeB.csv", "linear",
           Loiter( "usage", "==", 0.0),
           Modify( "usage", 1.0 ),
           Dawdle( Outputs(0) ),
           Modify( "usage", 0.0 ) )
Operation( "BGQ-core", "computeC", "computeC.csv", "linear",
           Loiter( "usage", "==", 0.0),
           Modify( "usage", 1.0 ),
           Dawdle( Outputs(0) ),
           Modify( "usage", 0.0 ) )

Mailbox( "BGQ-core", "unwait", lambda source, target, size, tag: [source],
         OnTarget )

Component( "BGQ-network" )
Attribute( "BGQ-network", "usage", 0.0 )
Operation( "BGQ-network", "transfer", "vulcan-transfer-512c.csv", "linear",
           Loiter( "usage", "==", 0.0),
           Modify( "usage", 1.0 ),
           Dawdle( Outputs(0) ),
           Modify( "usage", 0.0 ) )
Mailbox( "BGQ-network", "transfer", lambda source, target, size, tag: [size],
         OnAll )
Component( "BGQ-connection" )
Component( "system" )
#Offspring( "system", Tree( ["BGQ-network", "BGQ-core"], ["BGQ-connection"], [ cores ] ) )
Offspring( "system", Torus("BGQ-core", "BGQ-network", [8, 8, 8, 8, 4]) )
Root("system")

