#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH -t 1-
#SBATCH -J mesa_install
#SBATCH --mail-type=ALL
#SBATCH --mem-per-cpu=16G

export MESA_DIR=/gpfs/gibbs/project/bellinger/sk3365/Mesa/mesa

export OMP_NUM_THREADS=12

export MESASDK_ROOT=/gpfs/gibbs/project/bellinger/sk3365/Mesa/mesasdk

source $MESASDK_ROOT/bin/mesasdk_init.sh

export PATH=$PATH:$MESA_DIR/scripts/shmesa

module load make/4.3-GCCcore-10.2.0 Perl/5.32.0-GCCcore-10.2.0 X11/20201008-GCCcore-10.2.0 zlib/1.2.11-GCCcore-10.2.0 binutils/2.35-GCCcore-10.2.0 tcsh/6.22.03-GCCcore-10.2.0

cd $MESA_DIR
./install