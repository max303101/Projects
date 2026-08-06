// Made with Blockbench 4.9.4
// Exported for Minecraft version 1.17 or later with Mojang mappings
// Paste this class into your mod and generate all required imports


public class ModernCrossbow<T extends Entity> extends EntityModel<T> {
	// This layer location should be baked with EntityRendererProvider.Context in the entity renderer and passed into this model's constructor
	public static final ModelLayerLocation LAYER_LOCATION = new ModelLayerLocation(new ResourceLocation("modid", "moderncrossbow"), "main");
	private final ModelPart trigger;
	private final ModelPart string_right;
	private final ModelPart string_left;
	private final ModelPart bowarm_right;
	private final ModelPart bowarm_left;
	private final ModelPart crank;
	private final ModelPart right_holder;
	private final ModelPart left_holder;
	private final ModelPart arrow;
	private final ModelPart main;

	public ModernCrossbow(ModelPart root) {
		this.trigger = root.getChild("trigger");
		this.string_right = root.getChild("string_right");
		this.string_left = root.getChild("string_left");
		this.bowarm_right = root.getChild("bowarm_right");
		this.bowarm_left = root.getChild("bowarm_left");
		this.crank = root.getChild("crank");
		this.right_holder = root.getChild("right_holder");
		this.left_holder = root.getChild("left_holder");
		this.arrow = root.getChild("arrow");
		this.main = root.getChild("main");
	}

	public static LayerDefinition createBodyLayer() {
		MeshDefinition meshdefinition = new MeshDefinition();
		PartDefinition partdefinition = meshdefinition.getRoot();

		PartDefinition trigger = partdefinition.addOrReplaceChild("trigger", CubeListBuilder.create().texOffs(45, 53).addBox(-9.0F, -6.0F, 7.0F, 2.0F, 2.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(21, 5).addBox(-9.0F, -7.0F, 9.0F, 2.0F, 1.0F, 0.0F, new CubeDeformation(0.0F))
		.texOffs(23, 7).addBox(-7.0F, -7.0F, 8.0F, 0.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(49, 0).addBox(-9.0F, -6.0F, 4.5F, 2.0F, 1.0F, 2.5F, new CubeDeformation(0.0F))
		.texOffs(11, 46).addBox(-9.0F, -7.0F, 4.5F, 0.0F, 1.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(49, 36).addBox(-7.0F, -7.0F, 4.5F, 0.0F, 1.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(0, 26).addBox(-9.0F, -7.0F, 8.0F, 0.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(57, 25).addBox(-9.0F, -6.0F, 4.5F, 2.0F, 2.0F, 0.0F, new CubeDeformation(0.0F)), PartPose.offset(8.0F, 24.0F, -6.0F));

		PartDefinition string_right = partdefinition.addOrReplaceChild("string_right", CubeListBuilder.create().texOffs(0, 10).addBox(-0.5F, 0.0F, -0.5F, 12.0F, 0.0F, 1.0F, new CubeDeformation(0.0F)), PartPose.offset(-10.5F, 20.0F, -1.0F));

		PartDefinition string_left = partdefinition.addOrReplaceChild("string_left", CubeListBuilder.create().texOffs(0, 16).addBox(-11.75F, -1.0F, -0.5F, 12.0F, 0.0F, 1.0F, new CubeDeformation(0.0F)), PartPose.offset(10.75F, 21.0F, -1.0F));

		PartDefinition bowarm_right = partdefinition.addOrReplaceChild("bowarm_right", CubeListBuilder.create().texOffs(5, 58).addBox(-6.0F, -6.0F, 2.5F, 1.0F, 2.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(31, 5).addBox(-6.0F, -2.0F, 2.5F, 1.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(0, 18).addBox(-5.0F, -3.0F, 6.5F, 1.0F, 2.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(21, 27).addBox(-5.0F, -4.0F, 4.5F, 1.0F, 1.0F, 3.0F, new CubeDeformation(0.0F))
		.texOffs(25, 14).addBox(-5.0F, -2.0F, 4.5F, 1.0F, 1.0F, 2.0F, new CubeDeformation(0.0F)), PartPose.offset(-7.0F, 24.0F, -5.0F));

		PartDefinition cube_r1 = bowarm_right.addOrReplaceChild("cube_r1", CubeListBuilder.create().texOffs(8, 43).addBox(-7.9F, -2.0F, -4.4F, 3.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(52, 30).addBox(-7.9F, -3.0F, -4.4F, 3.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(51, 18).addBox(-7.9F, -5.0F, -4.4F, 3.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(23, 0).addBox(-13.9F, -3.0F, -6.4F, 9.0F, 2.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(47, 25).addBox(-7.9F, -4.0F, -6.4F, 3.0F, 1.0F, 3.0F, new CubeDeformation(0.0F))
		.texOffs(14, 18).addBox(-13.9F, -5.0F, -6.4F, 9.0F, 1.0F, 2.0F, new CubeDeformation(0.0F)), PartPose.offsetAndRotation(8.0F, 0.0F, -1.0F, 0.0F, 0.7854F, 0.0F));

		PartDefinition right_spring = bowarm_right.addOrReplaceChild("right_spring", CubeListBuilder.create().texOffs(42, 30).addBox(-1.5F, -4.0F, -1.5F, 3.0F, 2.0F, 3.0F, new CubeDeformation(0.0F)), PartPose.offset(-5.5F, 0.0F, 3.0F));

		PartDefinition bowarm_left = partdefinition.addOrReplaceChild("bowarm_left", CubeListBuilder.create().texOffs(5, 58).addBox(5.0F, -3.0F, 2.5F, 1.0F, 2.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(5, 58).addBox(5.0F, 1.0F, 2.5F, 1.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(0, 58).addBox(4.0F, 0.0F, 6.5F, 1.0F, 2.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(37, 55).addBox(4.0F, 1.0F, 4.5F, 1.0F, 1.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(28, 53).addBox(4.0F, -1.0F, 4.5F, 1.0F, 1.0F, 3.0F, new CubeDeformation(0.0F)), PartPose.offset(7.0F, 21.0F, -5.0F));

		PartDefinition cube_r2 = bowarm_left.addOrReplaceChild("cube_r2", CubeListBuilder.create().texOffs(54, 46).addBox(4.9F, -3.0F, -4.4F, 3.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(54, 53).addBox(4.9F, -2.0F, -4.4F, 3.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(0, 0).addBox(4.9F, -3.0F, -6.4F, 9.0F, 2.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(0, 48).addBox(4.9F, -4.0F, -6.4F, 3.0F, 1.0F, 3.0F, new CubeDeformation(0.0F))
		.texOffs(9, 55).addBox(4.9F, -5.0F, -4.4F, 3.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(0, 12).addBox(4.9F, -5.0F, -6.4F, 9.0F, 1.0F, 2.0F, new CubeDeformation(0.0F)), PartPose.offsetAndRotation(-8.0F, 3.0F, -1.0F, 0.0F, -0.7854F, 0.0F));

		PartDefinition left_spring = bowarm_left.addOrReplaceChild("left_spring", CubeListBuilder.create().texOffs(38, 44).addBox(-1.5F, -4.0F, -1.5F, 3.0F, 2.0F, 3.0F, new CubeDeformation(0.0F)), PartPose.offset(5.5F, 3.0F, 3.0F));

		PartDefinition crank = partdefinition.addOrReplaceChild("crank", CubeListBuilder.create().texOffs(13, 48).addBox(0.0F, -1.5F, -1.5F, 1.0F, 3.0F, 3.0F, new CubeDeformation(0.0F))
		.texOffs(26, 41).addBox(-2.0F, -1.5F, -1.5F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F)), PartPose.offset(-4.0F, 22.5F, 4.5F));

		PartDefinition right_holder = partdefinition.addOrReplaceChild("right_holder", CubeListBuilder.create().texOffs(9, 26).addBox(-3.0F, -0.6F, -1.0F, 3.0F, 1.0F, 2.0F, new CubeDeformation(0.0F)), PartPose.offset(-1.0F, 20.5F, -6.0F));

		PartDefinition left_holder = partdefinition.addOrReplaceChild("left_holder", CubeListBuilder.create().texOffs(37, 18).addBox(0.0F, -0.6F, -1.0F, 3.0F, 1.0F, 2.0F, new CubeDeformation(0.0F)), PartPose.offset(1.0F, 20.5F, -6.0F));

		PartDefinition arrow = partdefinition.addOrReplaceChild("arrow", CubeListBuilder.create(), PartPose.offset(0.0F, 19.0F, -5.0F));

		PartDefinition cube_r3 = arrow.addOrReplaceChild("cube_r3", CubeListBuilder.create().texOffs(2, 2).addBox(2.5F, 8.5F, -6.0F, 1.0F, 0.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 2).addBox(1.5F, 8.5F, 10.0F, 1.0F, 0.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 2).addBox(3.5F, 8.5F, 10.0F, 1.0F, 0.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(43, 33).addBox(1.5F, 8.5F, 8.0F, 3.0F, 0.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(43, 33).addBox(1.5F, 8.5F, -5.0F, 3.0F, 0.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(-9, -9).addBox(2.5F, 8.5F, -3.0F, 1.0F, 0.0F, 11.0F, new CubeDeformation(0.0F)), PartPose.offsetAndRotation(-3.9F, 9.0F, 0.0F, 0.0F, 0.0F, -2.3562F));

		PartDefinition cube_r4 = arrow.addOrReplaceChild("cube_r4", CubeListBuilder.create().texOffs(1, 2).addBox(7.0F, -3.0F, -5.0F, 1.0F, 0.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 2).addBox(9.0F, -3.0F, -5.0F, 1.0F, 0.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(43, 33).addBox(7.0F, -3.0F, -7.0F, 3.0F, 0.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(1, 2).addBox(8.0F, -3.0F, -21.0F, 1.0F, 0.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(43, 33).addBox(7.0F, -3.0F, -20.0F, 3.0F, 0.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(-9, -9).addBox(8.0F, -3.0F, -18.0F, 1.0F, 0.0F, 11.0F, new CubeDeformation(0.0F)), PartPose.offsetAndRotation(-3.9F, 9.0F, 15.0F, 0.0F, 0.0F, -0.7854F));

		PartDefinition main = partdefinition.addOrReplaceChild("main", CubeListBuilder.create().texOffs(0, 18).addBox(6.0F, 5.0F, -10.0F, 4.0F, 2.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(21, 7).addBox(7.0F, 4.0F, -10.0F, 2.0F, 1.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(55, 21).addBox(7.0F, 4.0F, -16.0F, 2.0F, 2.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(57, 12).addBox(10.0F, 5.0F, -16.0F, 1.0F, 2.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(0, 35).addBox(9.0F, 7.0F, -14.0F, 1.0F, 1.0F, 4.0F, new CubeDeformation(0.0F))
		.texOffs(54, 56).addBox(5.0F, 5.0F, -16.0F, 1.0F, 2.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(23, 56).addBox(10.0F, 5.0F, -12.0F, 1.0F, 2.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(56, 5).addBox(5.0F, 5.0F, -12.0F, 1.0F, 2.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(19, 42).addBox(9.0F, 4.0F, -5.0F, 1.0F, 4.0F, 4.0F, new CubeDeformation(0.0F))
		.texOffs(43, 8).addBox(8.0F, 5.0F, -5.0F, 1.0F, 3.0F, 4.0F, new CubeDeformation(0.0F))
		.texOffs(30, 46).addBox(9.0F, 4.0F, -1.0F, 1.0F, 2.0F, 4.0F, new CubeDeformation(0.0F))
		.texOffs(48, 40).addBox(8.0F, 5.0F, -1.0F, 1.0F, 1.0F, 4.0F, new CubeDeformation(0.0F))
		.texOffs(57, 0).addBox(8.0F, 4.0F, 2.0F, 1.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(42, 18).addBox(6.0F, 4.0F, -1.0F, 2.0F, 2.0F, 4.0F, new CubeDeformation(0.0F))
		.texOffs(41, 0).addBox(10.0F, 7.0F, -16.0F, 1.0F, 1.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(36, 39).addBox(10.0F, 5.0F, -15.0F, 5.0F, 2.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(0, 41).addBox(10.0F, 4.0F, -16.0F, 1.0F, 1.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(32, 12).addBox(6.0F, 7.0F, -14.0F, 3.0F, 1.0F, 4.0F, new CubeDeformation(0.0F))
		.texOffs(28, 39).addBox(5.0F, 7.0F, -16.0F, 1.0F, 1.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(18, 36).addBox(1.0F, 5.0F, -15.0F, 5.0F, 2.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(10, 36).addBox(5.0F, 4.0F, -16.0F, 1.0F, 1.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(34, 31).addBox(6.0F, 5.0F, -15.0F, 1.0F, 2.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(13, 27).addBox(7.0F, 4.0F, -15.0F, 2.0F, 3.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(34, 22).addBox(9.0F, 5.0F, -15.0F, 1.0F, 2.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(0, 26).addBox(6.0F, 4.0F, -5.0F, 2.0F, 4.0F, 4.0F, new CubeDeformation(0.0F))
		.texOffs(41, 7).addBox(5.0F, 6.0F, -4.0F, 1.0F, 1.0F, 1.0F, new CubeDeformation(0.0F)), PartPose.offset(-8.0F, 16.0F, 8.0F));

		PartDefinition cube_r5 = main.addOrReplaceChild("cube_r5", CubeListBuilder.create().texOffs(50, 7).addBox(-3.9F, -1.5F, -4.0F, 1.0F, 1.0F, 3.0F, new CubeDeformation(0.0F))
		.texOffs(55, 38).addBox(-3.0F, -1.5F, -4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(55, 41).addBox(-1.0F, -1.5F, -4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(22, 51).addBox(0.9F, -1.5F, -4.0F, 1.0F, 1.0F, 3.0F, new CubeDeformation(0.0F)), PartPose.offsetAndRotation(9.0F, 8.0F, -14.0F, 0.3927F, 0.0F, 0.0F));

		PartDefinition cube_r6 = main.addOrReplaceChild("cube_r6", CubeListBuilder.create().texOffs(38, 50).addBox(5.25F, -3.0F, -2.5F, 1.0F, 1.0F, 3.0F, new CubeDeformation(0.0F))
		.texOffs(51, 13).addBox(5.25F, -4.0F, -2.5F, 1.0F, 1.0F, 3.0F, new CubeDeformation(0.0F)), PartPose.offsetAndRotation(0.0F, 8.0F, -14.0F, 0.0F, 0.3927F, 0.0F));

		PartDefinition cube_r7 = main.addOrReplaceChild("cube_r7", CubeListBuilder.create().texOffs(52, 33).addBox(-6.25F, -4.0F, -2.5F, 1.0F, 1.0F, 3.0F, new CubeDeformation(0.0F))
		.texOffs(0, 53).addBox(-6.25F, -3.0F, -2.5F, 1.0F, 1.0F, 3.0F, new CubeDeformation(0.0F)), PartPose.offsetAndRotation(16.0F, 8.0F, -14.0F, 0.0F, -0.3927F, 0.0F));

		return LayerDefinition.create(meshdefinition, 64, 64);
	}

	@Override
	public void setupAnim(T entity, float limbSwing, float limbSwingAmount, float ageInTicks, float netHeadYaw, float headPitch) {

	}

	@Override
	public void renderToBuffer(PoseStack poseStack, VertexConsumer vertexConsumer, int packedLight, int packedOverlay, float red, float green, float blue, float alpha) {
		trigger.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
		string_right.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
		string_left.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
		bowarm_right.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
		bowarm_left.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
		crank.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
		right_holder.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
		left_holder.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
		arrow.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
		main.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
	}
}